pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/Jascandevelop/watson_language_translator', branch: 'master')
      }
    }

    stage('List') {
      steps {
        sh 'ls -la'
      }
    }

  }
}