pipeline {
    agent any
    stages {
        stage('pull') {
            steps{
            git 'https://github.com/skruvi/WorldOfGames.git'
         }
        }
        stage('Build') {
            steps{
            echo 'Docker image build'
            bat 'docker build -f ./Dockerfile . -t skruvi/worldofgames:latest'
         }
        }
        stage('Run') {
            steps{
                echo 'Start docker container'
                bat 'docker compose up -d'
            }
        }
        stage('Test') {
            steps{
                echo 'Testing...'
                bat (script: 'python e2e.py')
            }
        }
        stage('Close and publish'){
            steps {
                echo 'Stop the container'
                bat 'docker compose down'
                bat 'docker push skruvi/worldofgames:latest'
            }
        }
        }
    }