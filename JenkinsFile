pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
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
            echo 'Cleaning up...'
            sh "pkill -f app.py || true"
        }
    }
}
