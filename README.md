# PE 프로젝트 이름 (같이 정하기)
***
## INDEX
***
- [Description](#Description)
- [Prerequisite](#Prerequisite)
- [Usage](#Usage)
- [Environment](#Environment)
- [Files](#Files)
- [Contributing](#contributing)




## Description
***
We have created a module to extract and analyze customer-supplied data, especially a project to show and save information in graphs and csv files to make modulation performance of the modulator easier to see.
 
#### About PE
**If you use this README.md , you can use this function**
-  

## Prerequisite 설치해야할 소프트웨어
***
* Install pandas to process data. It is known as an essential library for tasks such as data analysis using Python.<http://pandas.pydata.org/pandas-docs/stable/>
* Install xml.etree.elemenTree. The module implements a simple and efficient API for parsing and creating XML data.
* Install numpy. Numpy is Python package that deals with numerical data. It is mainly used in linear algebra calculations using vectors and matrices via ndarray, a multidimensional matrix data structure called the core of Numpy.
* Install matplotlib.pyplot. Used to visualize data understanding prior to data analysis, or to visualize results after data analysis.
* Install lmfit. Lmfit provides a high-level interface to non-linear optimization and curve fitting problems for Python.
  <https://lmfit.github.io/lmfit-py/>
<!--
작성한 코드를 실행하기 전에 설치해야할 pakage나 의존성이 걸리는 문제
-->

## Usage 코드 실행 방법
***
Enter values for Wafer Option and Coordinate Option at run.py. After that, decide whether to save or show information.
<!--
작성한 코드를 어떻게 실행해야 하는지에 대한 가이드라인
Usage Example을 함께 작성
-->

## Environment 실행환경
***
* Python 3.8 
* GitHub Desktop Version 2.8.2 (x64)
* Windows 10 Home 20H2
<!--
실행환경에 대해 작성하면 된다. OS나 컴파일러 혹은 Hardware와 관련된 환경
-->

## Files
***
* src
  * directory.py - If there is no directory, it is a code that functions to create a new directory.
  * extract.py - It is a code that extracts information from a given xml data and has the ability to store it by replacing it with a file in csv format.
  * graph.py - Using the polyfit function, we obtain the polynomial closest to a given data and represent it in graphs.
  * path.py 
  * process.py - Based on the options received from run.py, the code is executed by selecting specific properties (image, wafer, image) from the data.
* gitignore   - Files that do not need to be managed in the project were managed using the gitignore file to exclude them from git.
* run.py      - It is the code that executes the project, and it receives several options to execute the Src file.
<!--
중요한 코드 파일들 몇 개를 대상으로 해당 파일이 어떠한 역할을 하는 파일인지를 간단히 설명해주면 전반적인 맥락을 파악하기에 좋을 것 같아 추가하였다.
-->

## Contributing - 사용자가 질문 할 수 있는 위치 지정 버그 생길시
이거는 좀 더 찾아봄 방법은 공부하긴했는데 오늘 내일 중으로 할게 
<!-- 
license 기입하기
-->