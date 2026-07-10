pipeline{
    agent any
    environment{
        IMAGE="fastapi-redis-cicd-app"
        CONTAINER="fastapi-redis-cicd"
        R="redis"
        NETWORK="jd_network"
    }
    stages{
        stage("Build FastAPI Image"){
            steps{
                sh "docker build -t ${IMAGE} ."
            }
        }

        stage("Remove FastAPI Container"){
            steps{
                sh """
                if docker ps -a --format '{{.Names}}' | grep -w ${CONTAINER}
                then
                docker rm -f ${CONTAINER}
                fi
                """
            }
        }

        stage("Remove Redis Container"){
            steps{
                sh """
                if docker ps -a --format '{{.Names}}' | grep -x "${R}"
                then
                docker rm -f ${R}
                fi
                """
            }
        }

        stage("Start Redis Container"){
            steps{
                sh "docker run -d --network ${NETWORK} --name ${R} ${R}:latest"
            }
        }

        stage("Start FastAPI Container"){
            steps{
                sh "docker run -d --name ${CONTAINER} --network ${NETWORK} ${IMAGE}"
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
