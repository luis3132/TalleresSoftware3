FROM maven:3.9.6-eclipse-temurin-22 AS maven

WORKDIR /app

COPY pom.xml .
COPY src ./src

RUN mvn clean package -DskipTests

FROM eclipse-temurin:22

WORKDIR /app

ENV BROKER_NAME=broker-1
ENV QUEUE_NAME=cola1

COPY --from=maven /app/target/producer-0.0.1-SNAPSHOT.jar ./producer.jar

CMD ["java", "-jar", "/app/producer.jar"]

EXPOSE 8081