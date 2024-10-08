# HotelPricePrediction Using Machine Learning
Developing a machine learning model to predict hotel prices based on factors such as star rating, review rating, and amenities offered by the hotel. By collecting and analyzing data from https://www.trivago.com/, the model will explore the relationships and correlations among these factors to accurately forecast hotel room prices.

<img src="https://github.com/user-attachments/assets/767e560c-0088-4e22-98bc-86a9b0e12db7" alt="image" height="300" width="600" />
<br><br><br>


<img src="https://github.com/user-attachments/assets/b9a61cca-5a5a-4665-bc36-d2aef9a58b5f" alt="image" height="300" width="600" />


## Tech Stack
| Tool             | Description                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Selenium         | Automated web scraping tool used to extract data from the Trivago website by locating elements using ID, class name, and XPath, and extracting text and attribute values. |
| PyCharm          | IDE used for developing Python scripts for data extraction, cleaning, and analysis.                                                                        |
| Microsoft Azure  | Cloud platform utilized to establish a data pipeline for effectively managing and securely storing scraped data in Azure Blob Storage.                     |
| REST API Postman | Tool used to create and test REST API endpoints, facilitating practical, real-time integration and application of the machine learning model.              |

## Sample DataSet
![image](https://github.com/user-attachments/assets/1348d7a2-f1e8-4175-b7ef-2aabf0d02716)

## Data Pipeline - Microsoft Azure
<img src="https://github.com/user-attachments/assets/57fadb70-c389-47fb-8ffb-f4279fb04a7a" alt="image" height="400" width="800" />

- **Hotel_Data**: This is the starting point, representing the input dataset that contains hotel-related information from scrapped_HotelsDataset.csv.

- **Clean Missing Data (clean_missing_data1)**: In the **Hotel Rating column**, the entire row which contains missing values is removed from the dataset. This ensures that only complete cases are used in subsequent analysis steps.

- **Summarize Data**:The data is summarized to understand its characteristics, such as mean, median, mode, and other descriptive statistics. This helps in gaining insights into the dataset before further processing.

- **Clean Missing Data (clean_missing_data_2)**: In the column **Review Rating**  null values  are replaced by the median of the column.

- **Split Data**: splits the dataset into two parts: 70% for training the model and 30% for testing it. This is important to validate the model's performance on unseen data.

- **Poisson Regression**: sets up the model to be used for analysis. Poisson regression is suitable for modeling count data and is often used in scenarios like predicting the number of bookings or events.

- **Train Model**: The model is trained using the training dataset. This step involves adjusting the model parameters to minimize error and improve predictions.

- **Select Columns in Dataset**: It involves selecting specific features or columns from the dataset that are relevant for model training. It helps in focusing the model on important data points.

- **Score Model**: After training, the model is evaluated on the test dataset to score its performance. This typically involves calculating metrics like accuracy, precision, recall, etc.

- **Evaluate Model**: Finally, this step evaluates the overall performance of the algorithm based on the scores from the test dataset. This is essential for understanding how well the model is likely to perform in real-world scenarios.
<br>

## Features found to have an impact on the target variable 
![feature](https://github.com/user-attachments/assets/b172af4e-c828-4848-b6e3-360fe308e1ab)

- **Selected Features**: Retained columns up to **"Review Rating"** with significant correlations.
  
- **Correlations** :Price, Hotel Rating, Pool, Hotel bar, Spa, Restaurant, Parking, Free WiFi , A/C, Review Rating.
  
- **Dropped Features**: Removed columns with low or no correlation : WiFi in lobby, Pets, Hotel Name.
  <br>

## Evaluation Metrics - Poisson Regression Algorithm
![evaluation_results](https://github.com/user-attachments/assets/2b4f864a-e707-4b87-9ada-802ebd39f2fa)

## Evaluation Metrics for the different ML Algorithms
<img src="https://github.com/user-attachments/assets/9d5cb860-7cdf-476c-af79-e5724c8c2512" alt="image" height="400" width="600" />

## How to Interpret
- Lower values of MAE and RMSE indicate better model performance.
- Higher values of R² indicate a better fit of the model to the data.

## Model Accuracies and Fine Tuning
- **Cleaning the Data**: Removing or imputing missing values, and correcting inconsistencies in the data . Feature Selection: Selecting the most relevant features using techniques like  Pearson correlation analysis  and dropping irrelevant features.
  
- **Model Selection**: Experimenting with different algorithms (e.g., linear ,Boosted Decision tree , Decision tree and poisson ) to find the best-performing one.
  
- **Poisson Regression** showed the best performance with a notable increase in accuracy with **62%**.

## Inference and Model Deployment - Postman

The JSON input sent via Postman includes details of the Hotel name, hotel rating (3.0), review rating 
(7.1), and available amenities (WiFi, restaurant, etc.). The specified price for this hotel is **4479**.

  ![postman input](https://github.com/user-attachments/assets/020bd615-d1d5-46b2-9ad1-a2a67902101f)
<br><br>
The JSON output received from the REST API contains the same hotel details and amenities, with an 
additional "Scored Labels" field showing the model-predicted price **4473.08**, providing a comparison 
to the actual price.
![postman result](https://github.com/user-attachments/assets/362fd98e-163c-475c-920f-019b3eb3eff2)

  
  











