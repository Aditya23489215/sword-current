from sklearn.linear_model import LinearRegression
from .models import Learning

def learning(age):
    age_list = [[object.x] for object in Learning.objects.all()]
    salary_list = [object.y for object in Learning.objects.all()]
    linearRegression=LinearRegression()
    linearRegression.fit(age_list, salary_list)
    prediction = linearRegression.predict([[age]])[0]
    coeff = linearRegression.coef_
    intercept = linearRegression.intercept_
    return (prediction, coeff, intercept)
