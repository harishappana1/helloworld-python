
pipeline {
    agent any

    parameters {
        choice(name:'DEPOLY_ENV', choices: ['dev', 'prod'], description: 'Select the deployment evironment')
    }

    stages{
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/harishappana1/helloworld-python.git'
            }
        }

        stage('Package') {
            steps {
                script {
                    bat 'powershell -Command "Compress-Archive -Path * -DestinationPath project.zip -Force"'
                }
            }
        }

        stage('Testing') {
            steps{
                echo "Testing..."
            }
        }

        stage('Deploy to Azure App Service') {
            steps {
                script {
                    bat 'az login --service-principal -u $CLIENTID -p $SECRET --tenant $TENANT'
                    bat 'az account set --subscription $SUBID'

                    if (params.DEPLOY_ENV == 'dev') {
                        bat 'az webapp deployment source config-zip --src project.zip --name dhaaps-dev --resource-group python-rg'
                    } else {
                        bat 'az webapp deployment source config-zip --src project.zip --name dhaaps-prod --resource-group python-rg'
                    }
                }
            }
        }
    }
}
