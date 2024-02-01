pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the GitHub repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Add your build commands here
                echo 'Building...'
                // For example: sh 'make build'
            }
        }

        stage('Test') {
            steps {
                // Add your test commands here
                echo 'Running tests...'
                // For example: sh 'make test'
            }
        }

        stage('Deploy') {
            steps {
                // Add your deployment commands here
                echo 'Deploying...'
                // For example: sh './deploy.sh'
            }
        }
    }

    post {
        always {
            // Steps to perform after the pipeline runs, regardless of the result
            echo 'Build completed.'
        }

        success {
            // Steps to perform if the pipeline is successful
            echo 'Build was successful!'
        }

        failure {
            // Steps to perform if the pipeline fails
            echo 'Build failed.'
        }
    }
}
