library(caTools)
library(rpart)
library(rpart.plot)
library(ROCR)
library(randomForest)
library(corrplot)
train_filename = "/Users/JoseCLee/Documents/GIT/datasci_course_materials/Kaggle/BikeSharingDemand/train.csv"
test_filename = "/Users/JoseCLee/Documents/GIT/datasci_course_materials/Kaggle/BikeSharingDemand/test.csv"
train = read.csv(train_filename)
test = read.csv(test_filename)
train$type = "train"
test$type = "test"
# Import training and testing data

# Add dummy values to test dataframe
test$casual = 0
test$registered = 0
test$count = 0

# Bind train and test data together
cdata = rbind(train, test)

# Convert some features to factors
cdata$season = as.factor(cdata$season)
cdata$holiday = as.factor(cdata$holiday)
cdata$workingday = as.factor(cdata$workingday)
cdata$weather = as.factor(cdata$weather)

# Extract hour, weekday, month, and year from datetime
datetime = as.POSIXlt(cdata$datetime)
hour = datetime$hour
weekday = as.factor(datetime$wday)
month = as.factor(datetime$mon)
year = 1900 + datetime$year
cdata$datetime = datetime

# Add the new features to the combined dataframe
cdata = cbind(cdata, hour, weekday, month, year)

# splitting data back to train & test
imputed_train = subset(cdata, type == "train")
imputed_test = subset(cdata, type == "test")
imputed_train$datetime = NULL
imputed_train$type = NULL
imputed_train$hour = as.factor(imputed_train$hour)
imputed_test
imputed_test$datetime = NULL
imputed_test$type = NULL
imputed_test$hour = as.factor(imputed_test$hour)
lm1 = lm(count ~ . - atemp - weekday - month - year , data= imputed_train)

RandomForestModel = randomForest(count ~ . - temp - weekday - month - year - casual - registered  - holiday - weekday, data= imputed_train)
RandomForestModel = randomForest(count ~ . , data= imputed_train)
importance(RandomForestModel)
RfPredict = round(predict(RandomForestModel, newdata=imputed_test),0)
LmPRedict = round(predict(lm1, newdata=imputed_test),0)
submission1 = data.frame(datetime = test$datetime, count = RfPredict)
submission2 = data.frame(datetime = test$datetime, count = LmPRedict)
write.csv(submission1, "/Users/JoseCLee/Documents/GIT/datasci_course_materials/Kaggle/BikeSharingDemand/submission1.csv", row.names=FALSE, quote = FALSE)
write.csv(submission2, "/Users/JoseCLee/Documents/GIT/datasci_course_materials/Kaggle/BikeSharingDemand/submission2.csv", row.names=FALSE, quote = FALSE)

library('Metrics')

rmsle(imputed_train$count, p)
p=round(predict(RandomForestModel),0)
p=round(predict(lm1),0)
predict(lm1)[1]
imputed_train$count[1]
