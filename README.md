# Apartment Finder

Context: My friends and I decided to sit down and look for apartments as the school year started to end. We went on tours throughout La Jolla and it was during one of these tours that I realized I really needed this
script. As we sat down, thinking about how amazing the place was, we were told that was taken. It then happened again the next day. There were no apartments with 3 bedrooms available anywhere. So I decided to create
a **Selenium + BeautifulSoup** script and run it on **Google Cloud**. Below is a tutorial.

1. To first test the local script, you can run main.py to start the **Flask** server. Then, use a curl command to see the result.
Ex:
```
curl -X POST <Server URL> \
-H "Content-Type: application/json" \
-d '{
    "urls": [
        "website 1",
        "website 2"
        "website 3"
    ]
}'
```

2. First, we will upload this script on **Google Cloud Functions**. This is a serverless environment for executing scripts. Great for something like an apartment finder to look for availability without always having your 
computer open. Copy and paste the code, but make sure you include the dependency requirements.

![image](https://github.com/hwu27/apartment_finder/assets/130116077/5c2bcb75-34ef-4f07-a954-c81d5474b515)

3. Next, we will use **Google Cloud Scheduler** to run the script every hour or so. Make sure that you are reading the websites terms and rules. Do not spam the website with requests. Check for a robots.txt file to check if they allow scraping. You can also add more staggered times
to send requests.

![image](https://github.com/hwu27/apartment_finder/assets/130116077/67e16959-c512-4f84-9451-8544a7aa924a)

4. We will then create a **Log-based Metric**, which is what we will want to check in our alert policy later

![image](https://github.com/hwu27/apartment_finder/assets/130116077/b49f14a2-983c-41ad-8a81-0d942148d105)

5. Lastly, we create our **Alert Policy**

![image](https://github.com/hwu27/apartment_finder/assets/130116077/09ac1a42-d123-499e-acf9-b29a79287d66)

Make sure to input the metric that we created right before

You can add notification channels in order to send alerts like emails, webhooks, etc.

