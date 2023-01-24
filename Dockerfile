FROM openjdk:17-jdk-slim as builder
ADD . /src
WORKDIR /src
RUN ./mvnw package -DskipTests

FROM openjdk:17-alpine
ENV JAVA_HOME=/opt/openjdk-17
ENV PATH="$PATH:$JAVA_HOME/bin"
COPY --from=builder /src/target/demo-start.jar app.jar
EXPOSE 9092
ENTRYPOINT ["java","-jar","/app.jar"]
