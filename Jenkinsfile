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
        stage('Uruchom aplikacje') {
            steps {
                sh 'pkill -f "python3 app.py" || true'
                sh 'JENKINS_NODE_COOKIE=dontKillMe nohup python3 app.py > app.log 2>&1 &'
                sh 'sleep 3 && curl -sf http://localhost:5000/'
                echo "Aplikacja dziala na porcie 5000 (srodowisko: ${params.SRODOWISKO})"
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
