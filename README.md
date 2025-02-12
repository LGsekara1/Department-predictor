## **Department predictor**

## **Introduction**
This tool gives a general idea of the departments that first year Univesity of Moratuwa undergrads. are most probable to apply.

NOTE: This is an experimental tool that uses a neural network trained on data based on 3 years undergrad. performance.

The tool takes the student index number to validate the identity and then uses GPA to analyse past data and give a prediction of the departments that the student is not eligible to apply for.

## **Features**
- Resposnive design.
- JS functionality for validation of input data and exlude departments that cannot be applied based on past data.
- Server-side processing with Flask framework (locally hosted) to access the ML model.
- The ML model was trained using a 2 layer feed forward neural network (64x32) 

## **Installation**
Since this is a static website no build is required. Download the repo and open the indexnew.html in a browser.
__OR__
1. Clone the repository.
2. Navigate into the project directory.
3. Start the flask app locally and make sure it runs on the correct port (localhost:5000). Use python backend.py to run in terminal.
4. Open the HTML file in the browser.

## **Contributing** 

1. Fork this repo.
2. Create a new branch (git checkout -b feature-name).
3. Make your changes and commit them (git commit -am "Add new feature").
4. Push to the branch (git push origin feature-name).
5. Create a new pull request.

## **License**
Department-predictor is released under the MIT License. See the **[LICENSE](LICENSE.txt)**



