pipeline {
    agent any
    // Check for changes in the SCM every minute
   triggers {
       pollSCM '* * * * *' // cada minuto consulta algun cambio en el repositorio de github
    }
    
    stages {
        stage('Run Python Script') {
            steps {
                sh '/var/jenkins_home/miniconda3/envs/PythonJenkins/bin/python3 view_machine_data.py'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
