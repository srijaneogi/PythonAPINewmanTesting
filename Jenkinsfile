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
                            timeout(10) {
                                def folder = new File( '${WORKSPACE}/newman1' )
                                println "Waiting for " + folder
                                println "folder==" + folder.exists()
				sh 'mkdir ${WORKSPACE}/newman1'
				sh 'ls -ltr'
                                waitUntil {
					def r = sh script: "[[ -d "${WORKSPACE}/newman1" ]]", returnStatus: true 
			           return r == 0                                       
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
