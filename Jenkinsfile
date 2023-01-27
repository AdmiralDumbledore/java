pipeline {
    agent any
    stages{
        stage('Build Project'){
            steps{
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/AdmiralDumbledore/java.git']])
                sh 'docker build . -t hello_spring_world:latest'
                sh 'docker tag hello_spring_world:latest 0401200104012001/java_test'
            }
        }
        stage('Push to DockerHub'){
            steps{
                withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerpwd')]) {
                sh 'docker login -u 0401200104012001 -p ${dockerpwd}'}
                sh 'docker push 0401200104012001/java_test'
            }
        }
    }
}