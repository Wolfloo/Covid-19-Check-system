# Covid-19-Check-system

## Introduce
This is a simple system for users check whether they are infected by Covid-19 or Viral Pneumonia. The train dataset comes from https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset/code?datasetId=627146&sortBy=voteCount .

The accuracy of the result in the test dataset is about 98%, however, due to the limitation of the dataset size, the result is for referance only.

## Quick Start

```
pip install -r requirements.txt
```

In the directory train_pred, you should execute the code named 'covid-19-classification-with-resnet50.ipynb' to train the model and get the model called 'model_resnet50.h5' . Then copy the model and paste it at ~\Covid-19-Check-system\web_system\utils\train_model.

Make sure you are in the folder '~\Covid-19-Check-system\web_system'

~~~
python .\manage.py runserver
~~~

## Snapshot

![image-20240410140557827](C:\Users\Dell\AppData\Roaming\Typora\typora-user-images\image-20240410140557827.png)

![image-20240410140746760](C:\Users\Dell\AppData\Roaming\Typora\typora-user-images\image-20240410140746760.png)

![image-20240410140812792](C:\Users\Dell\AppData\Roaming\Typora\typora-user-images\image-20240410140812792.png)







&nbsp;&nbsp; 
