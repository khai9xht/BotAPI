rm -rf rasa_test
mkdir rasa_test
pip install rasa --ignore-installed ruamel.yaml
cd rasa_test
rasa init --no-prompt
rasa run --enable-api