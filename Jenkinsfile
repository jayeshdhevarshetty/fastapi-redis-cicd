pipeline{
    agent any
        stage("Deploy"){
            steps{
                sh "docker compose down"
                sh "docker compose up -d --build"
            }
        }

        stage("Health Check"){
            steps{
                sh """
                sleep 5
                curl http://${CONTAINER}:8000/health
                """
            }
        }
    }
}