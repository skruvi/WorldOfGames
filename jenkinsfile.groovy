node any {
    cleanWs()
    stage('Build') {
        echo 'Docker image build'
        bat label: '', script: 'docker build -f ./Dockerfile . -t skruvi/worldofgames:latest'
    }
}