pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 demo2.py -coll_run Titan.postman_collection.json'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'newman/*.html'
            cleanWs()
        }
    }
}
