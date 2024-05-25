print('''
          M...m...m...M                              M...m...m...M
            MmmmmMmmmmM                                MmmmmMmmmmM
            MMmmMx""xMM                                MMx""xMmmMM
            Mmmmx    xM                                Mx    xmmmM
            MMmmx    xM                                Mx    xmmMM
   ss sss ssMmmmxxxxxxMsss  sss  sss  sss  sss  sss  ssMxxxxxxmmmMss sss sss sss s
   SS SSS SSMMx""xMmmMMSSS  SSS  SSS  SSS  SSS  SSS  SSMMmmMx""xMMSS SSS SSS SSS S
   SSssSSSssMx    xmmmMsssSSsssSSsssSSsssSSsssSSsssSSssMmmmx    xMSSsssSSsssSSsssS
   ssSSsssSSMx    xmmMMss""Sss""Sss""Sss""Sss""Sss""SssMMmmx    xMssSSSssSSSssSSSs
   SSssSSSssMxxxxxxmmmMSx  xSx  xSx  xSx  xSx  xSx  xSSMmmmxxxxxxMSSSssSSSssSSSssS
   ssSSsssSSMMmmMMMmmMMsxxxxsxxxxsxxxxsxxxxsxxxxsxxxxssMMmmMMMmmMMssSSSssSSSssSSSs
   SSssSSSssMmmmmMmmmmMSSsssSSsssSSs".mmm."SSsssSSsssSSMmmmmMmmmmMSSsssSSsssSSsssS
   ssSSsssSSMMmmMMMmmMMssSSSssSSSss"mMMMMMm"sSSSssSSSssMMmmMMMmmMMssSSSssSSSssSSSs
   SSssSSSssMmmmmMmmmmMSSsssSSsssSS.MMMMMMM.SsssSSsssSSMmmmmMmmmmMSSsssSSsssSSsssS
   ssSSsssSSMMmmMMMmmMMssSSSssSSSss.MMMMMMM.sSSSssSSSssMMmmMMMmmMMssSSSssSSSssSSSs
   SSssSSSsmMMMMMMMMMMMmSSSSSSSSSSS.MMMMMMM.SSSSSSSSSSmMMMMMMMMMMMmSsssSSsssSSssss
           MMMMMMMMMMMMM              ..              MMMMMMMMMMMMM           fsc

Welcome to the haunted castle, every choice counts, be careful, some paths might kill you, 
but the right one will grant you tons of gold.

''')

first_choice = input(
    "You enter the castle, there are two ways left and right, \none of them will make you closer to your goal, \nthe other is certain death, make a choice: Left(L) or Right(R)? ").upper()
if first_choice == "L":
    print('''
         \^~~~~\   )  (   /~~~~^/
          ) *** \  {**}  / *** (
           ) *** \_ ^^ _/ *** (
           ) ****   vv   **** (
            )_****      ****_(
              )*** m  m ***(

        ''')
    print("You went into a library and there are a few bats but you're alive.")
    second_choice = input(
        "Now you have two doors, a red door and a blue door, make a choice! Red(R) or Blue(B) ").upper()
    if second_choice == "B":
        print("There is a small door, you entered it")
        print(
            "You have two chests in front of you, you need to pick the right one, do you want the gold or the silver chest?")
        third_choice = input("Press S for the silver chest or G for the Gold chest ").upper()
        if third_choice == "S":
            print('''
                                                    _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           .'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|'      o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

                             ''')
            print("Congratulations, you found the treasure, you finished the game!")
            input("Press enter to leave the game ")


        else:
            print('''
                                      ,--.
                                   {    }
                                   K,   }
                                  /  ~Y`
                             ,   /   /
                            {_'-K.__/
                              `/-.__L._
                              /  ' /`\_}
                             /  ' /
                     ____   /  ' /
              ,-'~~~~    ~~/  ' /_
            ,'             ``~~~  ',
           (                        Y
          {                         I
         {      -                    `,
         |       ',                   )
         |        |   ,..__      __. Y
         |    .,_./  Y ' / ^Y   J   )|
         \           |' /   |   |   ||
          \          L_/    . _ (_,.'(
           \,   ,      ^^""' / |      )
             \_  \          /,L]     /
               '-_~-,       ` `   ./`
                  `'{_            )
                      ^^\..___,.--`

                      YOU'RE DEAD
            ''')
        input("Press enter to leave the game ")



    else:
        print('''
                                  ,--.
                               {    }
                               K,   }
                              /  ~Y`
                         ,   /   /
                        {_'-K.__/
                          `/-.__L._
                          /  ' /`\_}
                         /  ' /
                 ____   /  ' /
          ,-'~~~~    ~~/  ' /_
        ,'             ``~~~  ',
       (                        Y
      {                         I
     {      -                    `,
     |       ',                   )
     |        |   ,..__      __. Y
     |    .,_./  Y ' / ^Y   J   )|
     \           |' /   |   |   ||
      \          L_/    . _ (_,.'(
       \,   ,      ^^""' / |      )
         \_  \          /,L]     /
           '-_~-,       ` `   ./`
              `'{_            )
                  ^^\..___,.--`

                  YOU'RE DEAD
        ''')
    input("Press enter to leave the game ")




else:
    print('''
                              ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`

              YOU'RE DEAD
    ''')
input("Press enter to leave the game ")
