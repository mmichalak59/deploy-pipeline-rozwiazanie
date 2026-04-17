pipeline {
    agent any

    options {
        timeout(time: 15, unit: 'MINUTES')
    }

    parameters {
        choice(
            name: 'SRODOWISKO',
            choices: ['dev', 'staging', 'prod'],
            description: 'Srodowisko docelowe'
        )
    }

    stages {
        stage('Info') {
            steps {
                echo "Build: ${env.BUILD_NUMBER}"
                echo "Galaz: ${env.GIT_BRANCH}"
                echo "Srodowisko: ${params.SRODOWISKO}"
            }
        }
        stage('Testy') {
            steps {
                sh 'python3 test_app.py'
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t narzedzia:${env.BUILD_NUMBER} ."
            }
        }
        stage('Zatwierdzenie') {
            when {
                expression { params.SRODOWISKO == 'prod' }
            }
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            steps {
                input message: 'Czy na pewno wdrozyc na PRODUKCJE?',
                      ok: 'Tak, wdrazaj!'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop app-demo || true'
                sh 'docker rm app-demo || true'
                sh "docker run -d --name app-demo -p 5000:5000 narzedzia:${env.BUILD_NUMBER}"
                echo "Aplikacja wdrozona na ${params.SRODOWISKO} — port 5000"
            }
        }
    }

    post {
        success {
            echo "Build ${env.BUILD_NUMBER} wdrozony na ${params.SRODOWISKO}."
        }
        failure {
            echo "BLAD w buildzie ${env.BUILD_NUMBER}."
        }
    }
}
