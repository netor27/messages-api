import sys
from web import create_app

configFile = "config"
if len(sys.argv) > 1:
    configFile = sys.argv[1]

app = create_app(configFile, debug=True)

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000, debug=True)
