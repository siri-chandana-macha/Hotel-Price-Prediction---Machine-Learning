# HotelPricePrediction Using Machine Learning
Developing a machine learning model to predict hotel prices based on factors such as star rating, review rating, and amenities offered by the hotel. By collecting and analyzing data from https://www.trivago.com/, the model will explore the relationships and correlations among these factors to accurately forecast hotel room prices.

<img src="https://github.com/user-attachments/assets/767e560c-0088-4e22-98bc-86a9b0e12db7" alt="image" width="500" />


![image](https://github.com/user-attachments/assets/b9a61cca-5a5a-4665-bc36-d2aef9a58b5f)


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
![image](https://github.com/user-attachments/assets/57fadb70-c389-47fb-8ffb-f4279fb04a7a)

- **Hotel_Data**: This is the starting point, representing the input dataset that contains hotel-related information from scrapped_HotelsDataset.csv.

- **Clean Missing Data (clean_missing_data1)**: In the Hotel Rating column, the entire row which contains missing values is removed from the dataset. This ensures that only complete cases are used in subsequent analysis steps.

- **Summarize Data (summarize_data)**:The data is summarized to understand its characteristics, such as mean, median, mode, and other descriptive statistics. This helps in gaining insights into the dataset before further processing.

- **Clean Missing Data (clean_missing_data_2)**: In the column Review Rating  null values  are replaced by the median of the column.

- **Split Data (split_data)**: splits the dataset into two parts: 70% for training the model and 30% for testing it. This is important to validate the model's performance on unseen data.

- **Poisson Regression (poisson_regression)**: sets up the model to be used for analysis. Poisson regression is suitable for modeling count data and is often used in scenarios like predicting the number of bookings or events.

- **Train Model (train_model)**: The model is trained using the training dataset. This step involves adjusting the model parameters to minimize error and improve predictions.

- **Select Columns in Dataset (select_columns_in_dataset)**: It involves selecting specific features or columns from the dataset that are relevant for model training. It helps in focusing the model on important data points.

- **Score Model (score_model)**: After training, the model is evaluated on the test dataset to score its performance. This typically involves calculating metrics like accuracy, precision, recall, etc.

- **Evaluate Model (evaluate_model)**: Finally, this step evaluates the overall performance of the algorithm based on the scores from the test dataset. This is essential for understanding how well the model is likely to perform in real-world scenarios.
