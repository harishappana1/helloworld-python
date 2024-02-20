pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your repository
                git branch: 'main', url: 'https://github.com/harishappana1/helloworld-python.git'
            }
        }

        stage('Prepare Deployment Package') {
            steps {
                script {
                    // Use PowerShell to create a zip file of the project excluding the 'dummy' file
                    bat 'powershell -Command "Compress-Archive -Path * -DestinationPath project.zip -Force"'
                }
            }
        }

        stage('Deploy to Azure App Service') {
            steps {
                script {
                    bat 'az login --service-principal -u f7f3d431-c0a0-4a43-88d3-9af5cfa07bc4 -p Isb8Q~s~LXg8IMG7bdAIbFoS.IjncB5CJ_Xcjb5Y --tenant 7773a8cd-1747-47b4-8aea-3c19bab322ab'
                    
                    bat 'az account set --subscription cce3c17d-78f8-4ca8-bd35-958f2279a09b'
                    
                    bat 'az webapp deployment source config-zip --src project.zip --name dhappspython --resource-group python-rg'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully.'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
