import os
import main


if __name__ == '__main__':
    main.setup()
    embed_data_path = './data/w2v'
    if os.path.exists(embed_data_path) == False:
        main.embed_task()
    main.process_task(True, False)