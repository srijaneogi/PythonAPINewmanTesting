pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                
                sh 'python3 demo2.py -coll_run Titan.postman_collection.json'
            }
        }

    
    stage('wait') {
                    steps {
                        script {
                            timeout(2) {
                                def folder = new File( '${WORKSPACE}/newman' )
                                println "Waiting for " + folder
                                println "folder==" + folder.exists()
				sh 'mkdir ${WORKSPACE}/newman1'
				sh 'ls -ltr'
                                waitUntil {
					def exitCode = sh script: 'find . -name newman | egrep .', returnStatus: true
                                        boolean exists = exitCode == 0                                    
                                }
                            }
                        }
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
