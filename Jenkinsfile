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
        stage('Wdrozenie') {
            steps {
                script {
                    if (params.SRODOWISKO == 'dev') {
                        echo 'Wdrazam na DEV...'
                    } else if (params.SRODOWISKO == 'staging') {
                        echo 'Wdrazam na STAGING...'
                    } else {
                        echo 'Wdrazam na PRODUKCJE!'
                    }
                }
                echo "Wdrozenie na ${params.SRODOWISKO} zakonczone."
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
