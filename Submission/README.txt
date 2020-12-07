CS 145 Project
Team 31
Shaili Mathur, Aditya Pimplaskar, Ryan Wakefield, Tomer Laufer

Contents: 
- Team31.csv is our projections for Part 2 (12/6 - 12/13)

- SubmissionPt1.ipynb is a Jupyter notebook for our model to generate submission for Part 1

- SubmissionPt2.ipynb is a Jupyter notebook for our model to generate submission for Part 2

- Team31.yml environment file

- You can find the data that we used at the following link:
https://drive.google.com/drive/folders/1AWeI2UbTu1fs6I3qkR0vztVvg-CwpHyu?usp=sharing

Instructions:
1. Loading environment: 
conda env create -f environment.yml
conda activate team31
Packages needed are: pandas, numpy, statsmodels
  - To detach environment after: conda deactivate

2. Download data from the link above and store it in the same directory as these Jupyter notebooks

3. Can run all cells the notebooks directly

4. In order to generate the projected data files, you must uncomment the cell block that reads 
  #submission.to_csv('Team31_1.csv', index = False, header = True) in SubmissionPt1
  OR
  #submission.to_csv('Team31_2.csv', index = False, header = True) in SubmissionPt2
  - Note that the number following the underscore reflects the part of the project that the submission corresponds to. 

