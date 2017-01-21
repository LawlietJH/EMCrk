# -*- coding: utf-8 -*-
# Pagina: http://www.kammerl.de/ascii/AsciiSignature.php

import random

Banner1 = """
                                                      
                       ______ __  __  _____      _    
                      |  ____|  \/  |/ ____|    | |   
                      | |__  | \  / | |     _ __| | __
                      |  __| | |\/| | |    | '__| |/ /
                      | |____| |  | | |____| |  |   < 
                      |______|_|  |_|\_____|_|  |_|\_\\
                                                      
                                                        By: LawlietJH
"""
#(Font: 'big')


Banner2 = """
                                                                   
                                                                   
            `7MM'""YMM  `7MMM.     ,MMF' .g8'""bgd       `7MM      
              MM    `7    MMMb    dPMM .dP'     `M         MM      
              MM   d      M YM   ,M MM dM'       ``7Mb,od8 MM  ,MP'
              MMmmMM      M  Mb  M' MM MM           MM' "' MM ;Y   
              MM   Y  ,   M  YM.P'  MM MM.          MM     MM;Mm   
              MM     ,M   M  `YM'   MM `Mb.     ,'  MM     MM `Mb. 
            .JMMmmmmMMM .JML. `'  .JMML. `"bmmmd' .JMML. .JMML. YA.
                                                                   
                                                                By: LawlietJH
"""
#(Font: 'Georgia11')


Banner3 = """
                                                          
                ,------.,--.   ,--. ,-----.       ,--.    
                |  .---'|   `.'   |'  .--./,--.--.|  |,-. 
                |  `--, |  |'.'|  ||  |    |  .--'|     / 
                |  `---.|  |   |  |'  '--'\|  |   |  \  \ 
                `------'`--'   `--' `-----'`--'   `--'`--'
                                                        By: LawlietJH
"""
#(Font: 'soft')


Banner4 = """
                                                 
                         ___ __  __  ___     _   
                        | __|  \/  |/ __|_ _| |__
                        | _|| |\/| | (__| '_| / /
                        |___|_|  |_|\___|_| |_\_\\
                                                 
                                                    By: LawlietJH
"""
#(Font: 'small')


Banner5 = """
                                               
                         __|   \  |   __|      |  
                         _|   |\/ |  (      _| | /
                        ___| _|  _| \___| _|  _\_\\
                                              
                                                    By: LawlietJH
"""
#(Font: 'smshadow')


Banner6 = """
                                                    
            __________ ___       ___   ____           ___       
            `MMMMMMMMM `MMb     dMM'  6MMMMb/         `MM       
             MM      \  MMM.   ,PMM  8P    YM          MM       
             MM         M`Mb   d'MM 6M      Y ___  __  MM   __  
             MM    ,    M YM. ,P MM MM        `MM 6MM  MM   d'  
             MMMMMMM    M `Mb d' MM MM         MM69 "  MM  d'   
             MM    `    M  YM.P  MM MM         MM'     MM d'    
             MM         M  `Mb'  MM MM         MM      MMdM.    
             MM         M   YP   MM YM      6  MM      MMPYM.   
             MM      /  M   `'   MM  8b    d9  MM      MM  YM.  
            _MMMMMMMMM _M_      _MM_  YMMMM9  _MM_    _MM_  YM._
                                                    
                                                    
                                                        By: LawlietJH
"""
#(Font: 'georgi16')


Banner7 = """
                               *                   
                             (  `     (          ) 
                         (   )\))(    )\  (   ( /( 
                         )\ ((_)()\ (((_) )(  )\())
                        ((_)(_()((_))\___(()\((_)\ 
                        | __|  \/  ((/ __|((_) |(_)
                        | _|| |\/| || (__| '_| / / 
                        |___|_|  |_| \___|_| |_\_\ 
                                                    By: LawlietJH
"""
#(Font: 'fire_font-s')


Banner8 = """
                                                                
                8888888888888b     d888 .d8888b.        888     
                888       8888b   d8888d88P  Y88b       888     
                888       88888b.d88888888    888       888     
                8888888   888Y88888P888888       888d888888  888
                888       888 Y888P 888888       888P"  888 .88P
                888       888  Y8P  888888    888888    888888K 
                888       888   "   888Y88b  d88P888    888 "88b
                8888888888888       888 "Y8888P" 888    888  888
                                                
                                                            By: LawlietJH
"""
#(Font: 'colossal')


Banner9 = """




Banner10 = """


def Banner():
    Banners = [ Banner1, Banner2, Banner3, Banner4, Banner5,\
				Banner6 ]
    return random.choice(Banners)
