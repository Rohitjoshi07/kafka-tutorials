# KAFKA INSTALLATION IN WINDOWS #

Refer below steps to install kafka in windows machine. These instructions are defined to setup the kraft implementation of Kafka, which is a replacement to zookeeper since kafka version 3.3

We can run kafka in windows usin WSL(window subsystem for linux) or Docker, here we will setup using WSL.

## STEP 1: SETUP JDK
To run kafka we need to first setup the jdk in your machine.
Check availabily using `<java -version>` in your terminal.
If not present than install and setup using below steps:

1. Go to https://www.oracle.com/java/technologies/downloads/#jdk21-windows, and download the appropriate JDK version as per your system configuration.
2. Once download, extract the files and run installer executable.
3. Select JDK component(JRE is optional) when prompt.
4. Set these two environment variables: In PATH add `<C:\Program Files\Java\jdk1.8.0_281\bin>` and  set JAVA_HOME as `<C:\Program Files\Java\jdk1.8.0_281>`, here navigate to directory where you have your jdk folder.
5. verify installation by running `<java -version>` in terminal.

## STEP 2: INSTALL WSL
1. Check the apps in setting if windows subsystem for linux is alredy present.
2. If not then open terminal and write `<wsl --install>` and choose ubuntu or you can download ubuntu from the microsoft store.
3. Checkout https://learn.microsoft.com/en-us/windows/wsl/install if you face any issues.

## STEP 3: Install Kafka
1. Go to https://kafka.apache.org/downloads and download any scala binary of latest stable version, kafka version>3.3 for kraft.
2. Extract the files once downloaded and keep at your preferred place.

## STEP 4: Setup and Run Kafka Cluster
1. Open terminal from kafka directory.
2. Execute `<.\bin\windows\kafka-storage.bat random-uuid>` to generate the unique id for kafka cluster.
3. Format the log storage and setup the unique id in kraft server by executing `<.\bin\windows\kafka-storage.bat format -t unique-id-form-above -c .\config\kraft\server.properties>`
4. Run kafka server: `<.\bin\windows\kafka-server-start.bat .\config\kraft\server.properties>`

## STEP 5: CREATE KAFKA TOPIC and Start KAFKA PRODUCER
1. Open another terminal from kafka\bin\windows
2. Create topic: `<.kafka-topics.bat --create --topic topic-name --bootstrap-server localhost:9092>`
3. Once the topic is created start the producer using: `<kafka-console-producer.bat --topic topic-name --bootstrap-server localhost:9092>`

## STEP 6: START KAFKA CONSUMER
1. Open another terminal from the windows directory.
2. Start Kakfa consumer: `<kafka-console-consumer.bat --topic topic-name --bootstrap-server localhost:9092>`
3. Use --from-beginning flag if you want to read all the previous messages of the topic too.
4. Once consumer starts any message you sent from produver will reflect in consumer console.


So with above steps you can setup and run kafka in windows. 
