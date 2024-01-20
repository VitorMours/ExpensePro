import App
import sys
import argparse
from dotenv import dotenv_values
from flask import Flask, jsonify, request

def run_app(app_mode="default"):
    match app_mode:
        # TODO: Fazer Modificação e instanciamento de cada uma das partes do aplicativo
        # correspondente a flag à qual foi designada.
        case "web":
            pass
        case "api":
            pass
        case "test":
            pass
        case _:
            app = App.create_app()
            env_config = dotenv_values(".env")
            host = env_config["HOST"]
            port = env_config["PORT"]

            app.run(host=host, port=port, use_reloader=False)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    prog=f"main.py: CLI to launch application by the command line.",
    description="Descrição do projeto",
    epilog="Any question email to jvrezendemoura@gmail.com")
    
    arguments_dict = {
    "--web":"launching only the web part of the project",
    "--api":"launching only the api and the endpoints",
    "--test":"testing the application to search for any necessity"}
    
    for argument, description in arguments_dict.items():
        parser.add_argument(argument,f"{argument[0]}{argument[2]}", help=description, action="store_true")

    parser.add_argument("--default", "-d", 
                        help="launching the app in the default mode, both API and website gonna be launch",
                        action="store_true")
    
    args = parser.parse_args()
    print(args)

    for k, v in (vars(args)).items():
        if v:
            run_app(str(k))    
            break
        else: run_app()













    # print(sys.argv)
    # if len(sys.argv) == 1:
    #     run_app()
    # else:
    #     match sys.argv[1].lower():
    #         case "api":
    #             print("Subindo aenas api")
    #         case "web":
    #             print("Subindo apenas web")
            
    #         case _:
    #             print("""Esse tipo de argumento não é válido, ou existente dentro desse programa.\n
    #             Lançando aplicação web com API.""")

