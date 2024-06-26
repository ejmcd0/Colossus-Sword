def title_art():
    title = r"""
       ___      _                           __                       _ 
      / __\___ | | ___  ___ ___ _   _ ___  / _\_      _____  _ __ __| |
     / /  / _ \| |/ _ \/ __/ __| | | / __| \ \\ \ /\ / / _ \| '__/ _` |
    / /__| (_) | | (_) \__ \__ \ |_| \__ \ _\ \\ V  V / (_) | | | (_| |
    \____/\___/|_|\___/|___/___/\__,_|___/ \__/ \_/\_/ \___/|_|  \__,_|
                                                    
    """
    print(title)

def enemy_art(enemy):
    #enemy = ["demon", "troll", "dark elf", "mage", "cyborg", "unknown"]
    if enemy == "Demon":
        return r"""
         .-._                                                   _,-,
          `._`-._                                           _,-'_,'
             `._ `-._                                   _,-' _,'
                `._  `-._        __.-----.__        _,-'  _,'
                   `._   `#==="""           """===#'   _,'
                      `._/)  ._               _.  (\_,'
                       )*'     **.__     __.**     '*( 
                       #  .==..__  ""   ""  __..==,  # 
                       #   `"._(_).       .(_)_."'   #
        """

    elif enemy == "Troll":
        return r"""
              -. -. `.  / .-' _.'  _
             .--`. `. `| / __.-- _' `
            '.-.  \  \ |  /   _.' `_
            .-. \  `  || |  .' _.-' `.
          .' _ \ '  -    -'  - ` _.-.
           .' `. %%%%%   | %%%%% _.-.`-
         .' .-. ><(@)> ) ( <(@)>< .-.`.
           (("`(   -   | |   -   )'"))
          / \\#)\    (.(_).)    /(#//\
         ' / ) ((  /   | |   \  )) (`.`.
         .'  (.) \ .md88o88bm. / (.) \)
           / /| / \ `Y88888Y' / \ | \ \
         .' / O  / `.   -   .' \  O \ \\
          / /(O)/ /| `.___.' | \\(O) \
           / / / / |  |   |  |\  \  \ \
           / / // /|  |   |  |  \  \ \
         _.--/--/'( ) ) ( ) ) )`\-\-\-._
        ( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) )
        
        """
    #print(troll)


    elif enemy == "Dark Elf":
        return r"""
                     ..-.--..
                   ,','.-`.-.`.
                  :.',;'     `.\.
                  ||//----,-.--\|
                \`:|/-----`-'--||'/
                 \\|:    |:'
                  `||      \   |!
                  |!|          ;|
                  !||:.   --  /|!
                 /||!||:.___.|!||\
                /|!|||!|    |!||!\\:.
             ,'//!||!||!`._.||!||,:\\\
            : :: |!|||!| SSt|!||! |!::
            | |! !||!|||`---!|!|| ||!|
            | || |!|||!|    |!||! |!||
        
        """
    #print(darkElf)

    elif enemy == "Mage":
        return r"""
                        ____ 
                      .'* *.'
                   __/_*_*(_
                  / _______ \
                 _\_)/___\(_/_ 
                / _((\- -/))_ \
                \ \())(-)(()/ /
                 ' \(((()))/ '
                / ' \)).))/ ' \
               / _ \ - | - /_  \
              (   ( .;''';. .'  )
              _\"__ /    )\ __"/_
                \/  \   ' /  \/
                 .'  '...' ' )
                  / /  |  \ \
                 / .   .   . \
                /   .     .   \
               /   /   |   \   \
             .'   /    b    '.  '.
         _.-'    /     Bb     '-. '-._ 
     _.-'       |      BBb       '-.  '-. 
    (________mrf\____.dBBBb.________)____)
    """
    #print(mage)


    elif enemy == "Cyborg":
        return """
    ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣴⣾⣿⠿⠟⠛⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀
    ⠀⠀⣼⣿⠟⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀
    ⠀⣸⣿⠇⣠⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀
    ⠀⣿⣿⠀⣿⣿⠀⠀⠉⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
    ⠀⣿⣿⢸⣿⡏⠀⠀⢸⣿⠁⠈⣻⣿⣿⣿⣿⣿⣿⣿⡇⠀
    ⢰⣿⣿⣿⣿⣤⣤⣀⣈⠻⣷⣾⣿⣿⡿⠟⠉⢹⣿⣿⣷⡆
    ⢸⣿⣿⡏⠀⠉⠙⠿⠿⠇⣿⣿⣿⣁⣀⠀⠀⢘⣿⣿⣿⡇
    ⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
    ⠀⢸⣿⡇⠀⠀⠀⠀⢀⣀⡀⢀⣈⡙⠻⣿⣿⣿⣿⣿⠁⠀
    ⠀⠈⣿⡇⠀⠀⠀⠀⠈⠉⠻⠟⠉⠁⠀⠈⢿⣿⣿⣿⠀⠀
    ⠀⠀⠻⣿⣦⡀⠀⠀⣠⣴⡶⢶⣦⣄⠀⠀⢀⣿⣿⠏⠀⠀
    ⠀⠀⠀⠈⠻⣿⣦⡀⠈⠀⠀⠀⠈⠁⢀⣴⣿⠟⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀
    
    """
    #print(cyborg)


    elif enemy == "Unknown":
        return r"""
                                                 ,--,  ,.-.
                   ,                   \,       '-,-`,'-.' | ._
                  /|           \    ,   |\         }  )/  / `-,',
                  [ ,          |\  /|   | |        /  \|  |/`  ,`
                  | |       ,.`  `,` `, | |  _,...(   (      .',
                  \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\
                   \  \_\,``,   ` , ,  /  |         )         _,/
                    \  '  `  ,_ _`_,-,<._.<        /         /
                     ', `>.,`  `  `   ,., |_      |         /
                       \/`  `,   `   ,`  | /__,.-`    _,   `\
                   -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                    \_,,.) /\    ` /  / ) (-,, ``    ,        |
                   ,` )  | \_\       '-`  |  `(               \
                  /  /```(   , --, ,' \   |`<`    ,            |
                 /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
           ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
          (-, \           ) \ ('_.-._)/ /,`    /
          | /  `          `/ \\ V   V, /`     /
       ,--\(        ,     <_/`\\     ||      /
      (   ,``-     \/|         \-A.A-`|     /
     ,>,_ )_,..(    )\          -,,_-`  _--`
    (_ \|`   _,/_  /  \_            ,--`
     \( `   <.,../`     `-.._   _,-`
     """

    #return enemy

