import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
import warnings
from lmfit import Parameters, fit_report, minimize, Model
from . import path
from . import directory


def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['determination'] = ssreg / sstot
    return results


def IV(x, Is, vt):
    return Is * (exp(x / vt) - 1)


def graph(route, save, show):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', np.RankWarning)
        tree = parse(str(route))
        root = tree.getroot()
        plt.figure(figsize=(16, 10))

        # IV Measurement
        plt.subplot(2, 3, 4)
        voltage = list(map(float, root.find('.//IVMeasurement/Voltage').text.split(',')))
        current = list(map(float, root.find('.//IVMeasurement/Current').text.split(',')))
        v = np.array(voltage)
        c = np.array(current)
        gmodel = Model(IV)
        params = gmodel.make_params(Is=1, vt=0.026)
        result = gmodel.fit(c, params, x=v)

        c2 = c - result.best_fit
        IV_Rsq = {}
        for i in range(1, 20):
            poly = polyfit(v, c2, i)
            IV_Rsq[i] = poly['determination']
        IV_max_key = max(IV_Rsq, key=lambda key: IV_Rsq[key])
        global IV_max_rsq
        IV_max_rsq = IV_Rsq[IV_max_key]
        polyIV = np.poly1d(np.polyfit(v, c2, IV_max_key))(v)

        plt.plot(v, abs(c), 'ok')
        plt.plot(v, abs(result.best_fit + polyIV), '--', label='Highest order term = {}'.format(IV_max_key))
        plt.legend(loc='best')
        plt.xlabel('Voltage[V]')
        plt.ylabel('Current[A]')
        plt.title('IV-analysis')
        plt.yscale('log')

        # Raw Spectrum
        plt.subplot(2, 3, 1)
        TestSiteInfo = root.find('TestSiteInfo')
        TestSite = TestSiteInfo.attrib['TestSite']
        ModulatorName = ".//*[@Name='{}_ALIGN']//".format(TestSite)
        ref_L = list(map(float, root.findtext(str(str(ModulatorName + 'L'))).split(',')))
        ref_IL = list(map(float, root.findtext(str(str(ModulatorName + 'IL'))).split(',')))
        global max_IL
        max_IL = max(ref_IL)
        for wavelengthsweep in root.iter('WavelengthSweep'):
            L = list(map(float, wavelengthsweep.findtext('L').split(',')))
            IL = list(map(float, wavelengthsweep.findtext('IL').split(',')))
            if IL == ref_IL:
                name = 'Reference'
            else:
                name = 'DCBias=' + str(wavelengthsweep.attrib['DCBias']) + 'V'
            plt.plot(L, IL, 'o', label=name)

        plt.legend(loc='lower right')
        plt.xlabel('Wavelength[nm]')
        plt.ylabel('Measured transmissions[dB]')
        plt.title('Transmission spectra - as measured')

        # Fitting
        plt.subplot(2, 3, 3)
        x = np.array(ref_L)
        y = np.array(ref_IL)

        plt.scatter(x, y, facecolor='none', edgecolor='r', alpha=0.06, label='Reference')
        ref_Rsq = {}
        for i in range(4, 7):
            poly = polyfit(x, y, i)
            ref_Rsq[i] = poly['determination']
            fit = np.poly1d(poly['polynomial'])(x)
            plt.plot(x, fit, label='Highest order term =' + str(i) + '\nR^2 = ' + str(poly['determination']))

        ref_max_key = max(ref_Rsq, key=lambda key: ref_Rsq[key])
        global ref_max_Rsq
        ref_max_Rsq = ref_Rsq[ref_max_key]
        plt.legend(loc='lower right')
        plt.xlabel('Wavelength[nm]')
        plt.ylabel('Measured transmissions[dB]')
        plt.title('Fitting Function')

        # Modeling
        plt.subplot(2, 3, 2)
        ref = np.poly1d(np.polyfit(x, y, ref_max_key))
        for wavelengthsweep in root.iter('WavelengthSweep'):
            L = list(map(float, wavelengthsweep.findtext('L').split(',')))
            IL = list(map(float, wavelengthsweep.findtext('IL').split(',')))
            l = np.array(L)
            il = np.array(IL)
            if IL == ref_IL:
                name = 'Reference'
            else:
                name = 'DCBias=' + str(wavelengthsweep.attrib['DCBias']) + 'V'
            plt.plot(l, il - ref(l), label=name)

        image_path = route.replace("\\", "/").split("/")
        sub_path = ''
        for i in range(-4, -1):
            sub_path += '/' + image_path[i]
        plt.legend(loc='lower right')
        plt.xlabel('Wavelength[nm]')
        plt.ylabel('Transmissions[dB]')
        plt.title('Transmission spectra - fitted')
        save_path = path.path() + '/result/graph/lot' + sub_path
        directory.create_folder(save_path)

        if show is True:
            plt.show()
        if save is True:
            plt.savefig(save_path + '/' + image_path[-1] + '.png')
        plt.close()