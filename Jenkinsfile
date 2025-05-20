pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Check Python') {
            steps {
                sh 'which pip'
                sh 'which python3'
                sh 'pip --version'
                sh 'python3 --version'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Start Web App') {
            steps {
                sh 'nohup python app.py &'
                sh 'sleep 5'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'python test_login.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up application'
            sh "pkill -f app.py || true"
        }
    }
}
