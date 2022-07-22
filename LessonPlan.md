# Backend 13.2 - HTTP methods

This lesson plan template is aimed at preparing instructors to deliver a high quality live session to learners who have already prepared to work on the project by setting up any prerequisites before coming to class.

## Prep List

- [ ] Watch the lesson plan overview video. ***Link to be included once lesson plan is complete***
- [ ] After watching the lesson overview, internalize lesson plan in full
- [ ] Set up your local machine to be prepared to teach the live session as follows:
    - Download and install PyCharm
    - Download and install ngrok
- [ ] If you are running code in your live session, make sure it works and the solution code is accurate
- [ ] If your lesson plan includes technical steps, be sure to have walked through them first before teaching

## Lesson Plan

### 1. Engage Classroom (1-2 min.)

- ***Remind learners of classroom expectations during live Code-Along instruction:***
  - Web cameras need to be on to have the best learning experience possible
  - Talk about how we are going to be using specific communication tools like Slido, Zoom, etc. during the live session
  - If you need additional technical support that goes beyond this Code-Along, please use the Hub's knowledge base to start or schedule 1:1 support

- ***Pick one activity*** to help build an online community here at BloomTech and get learners excited for live instruction:
  - ***Icebreaker:*** Fun activity that helps learners get to know one another
  - ***Pulse Check:*** Pose a question for learners to gauge how they are feeling/get a pulse on how where they are at this point in the course
  - ***Do Now:*** Pose a question that involves no guidance from you. Used to activate students’ learning for the lesson, surface prior knowledge from pre-work, and familiarize students with today’s content
  - ***Celebrations:*** Share a learner celebration, job offer, remind students why they are putting in all this hard work


### 2. Getting Started (3-5 min.)

- State that the learners should have already setup their gitbash (for Windows users only) before joining this live session
- Remind learners what they’ve worked on up until now to get to this point within the sprint
  - DynamoDB (load, read, write)
  - HTTP methods and how they map to CRUD operations
  - REST API
  - CURL commands
  - How data is sent as part of HTTP method calls - path paramter, query string parameter and request body.
- Utilize a metaphor or an analogy to get learners excited to learn the key concepts
  - Let’s say that a regular calculator is an API. You send a “2+2” Operation as a Request, hit the equal button, and receive a “4” as a Response. You’re not interested in how the calculator processed this information; you just want an accurate response to the Inputs and Operation that you sent in the Request. In today's code along we will use curl commands to make such an api call.
- Highlight the key concepts that will be covered during the live session
  - HTTP methods and how they map to CRUD operations
  - REST API
  - CURL commands
- Explain how these concepts are designed with the sprint challenge in mind and how it’s critical to the job
  - Writing APIs are one of the most common tasks a backend developer does. Using these curl commands is how we generally test these APIs.

### 3. What Will We Be Building In This Code-Along? (2-3 min.)

We will be using CURL commands to make API calls. 
As an instructor, I am going to start a server at my end and you are going to call the API using curl commands. We will be practicing using GET, POST and PUT HTTP methods to make these calls.


***Preview End Result:*** 
```
- GET: curl <url>
- POST: curl -X POST <url> -d '{"username":"1", "answer":"my answer"}'
- PUT: curl -X PUT <url>/me -d '{"answer":"my answer"}'
```

### 4. Let’s Build (30 min.)


- **Problem:** We want to make an API call and get the question to be answered. Then, post the answer to the question and also update it.

- **Solution:** Write the GET, POST and PUT curl commands and execute them in terminal/gitbash.

- **Build It:** 
  
   - **Step 1:**  Making the GET curl request
     - We make the GET request when we want to read something.
     - Start the Python get_server.py (given in the repository). <br/>
     - In your terminal / gitbash, run the following command to start ngrok:
       ```
       ngrok http 8000
       ```
     - Share the forwarding URL from your ngrok terminal.
     - Now, ask the learners to write the curl command in their terminals and connect to your http get_server. As the learners start making requests, you would be able to see those requests in your ngrok terminal as well as in python output window.
        - Sample Curl command:
        ```
       curl <forwarding url you shared above>:8000
       ```
     - Learners should receive a random question as the response to their API calls. (All the questions are listed in get_server.py)

   - **Step 2:**  Making the POST curl request
     - We make the POST request when we want to create a new entry.
     - Start the Python post_server.py (given in the repository). <br/>
     - In your terminal / gitbash, run the following command to start ngrok:
       ```
       ngrok http 8001
       ```
     - Share the forwarding URL from your ngrok terminal.
     - Now, ask the learners to write the curl command in their terminals and connect to your http post_server. Remind them that to make the POST request 
        - they will be sending data in the request body and we use '-d' option to send the request body data in curl command. 
        - Data should be 'username' and 'answer' to the question they had received in the GET request. 
        - Also, this data is going to be in json format.
        - And, we use '-X' option to specify the HTTP method.
        As the learners start making requests, you would be able to see those requests in your ngrok terminal as well as in python output window.
        - Sample Curl command:
       ```
       curl -X POST <forwarding url you shared above>:8001  -d '{"username":"1", "answer":"my answer"}'
       ```
     - Learners should receive a success message and you can share your python output window to show the entries being created.
     
   - **Step 3:**  Making the PUT curl request
     - We make the POST request when we want to update an existing entry.
     - Start the Python put_server.py (given in the repository). <br/>
     - In your terminal / gitbash, run the following command to start ngrok:
       ```
       ngrok http 8002
       ```
     - Share the forwarding URL from your ngrok terminal.
     - Now, ask the learners to write the curl command in their terminals and connect to your http put_server. Remind them that to make the PUT request 
        - They will be sending the new answer in the request body using '-d' in curl command. 
        - Data should be 'new answer' to the question they had received in the GET request. 
        - And, the username will be sent as path parameter.
        - Also, this data is going to be in json format.
        - And, we use '-X' option to specify the HTTP method.
        As the learners start making requests, you would be able to see those requests in your ngrok terminal as well as in python output window.
        - Sample Curl command:
       ```
       curl -X PUT <forwarding url you shared above>:8002/<username>  -d '{"answer":"new answer"}'
       ```
     - Learners should receive a success message and you can share your python output window to show the entries.


### 5. Wrap Up (7-10 min.)

- ***Answer questions*** in a question and answer format, time permitting
- ***Restate*** the key concepts and why the project was important to the job
Q&A for the whole project time permitting
- ***Review*** next steps in the learner journey as it relates to the sprint of learning.  Example:  If you are in Code-Along 1, you would encourage the learner to spend time with the next two learning modules before attending Code-Along 2 for this sprint
- ***Encourage*** learners to sign up for another live Code-Along or repeat this one if they want to review it again
