pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Start Web App') {
            steps {
                sh 'nohup python3 app.py &'
                sh 'sleep 5'
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'python3 test_login.py'
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
