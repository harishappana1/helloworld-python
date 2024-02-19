pipeline {
    agent any

    environment {
        AZURE_WEBAPP_NAME = 'pytohnharish'
        AZURE_RESOURCE_GROUP = 'python-rg'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/harishappana1/helloworld-python.git'
            }
        }

        stage('Deploy to Azure Web App') {
            steps {
                script {
                    sh 'cp app.py requirements.txt $AZURE_WEBAPP_NAME/'
                    azureWebAppDeploy azureCredentialsId: 'python-sp',
                                      resourceGroup: "${AZURE_RESOURCE_GROUP}",
                                      appName: "${AZURE_WEBAPP_NAME}"
                }
            }
        }
    }
}
