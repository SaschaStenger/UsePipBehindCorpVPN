# UsePipBehindCorpVPN
Some corporate VPNs will meddle with Pip certificates and will prevent package installation. With this, it is possible to tell python, that the provided vertificat of your company is a valid one. 

# UsePipBehindCorpVPN
Some corporate VPNs will meddle with Pip certificates and will prevent package installation. With this, it is possible to tell python, that the provided vertificat of your company is a valid one. 


1.) Installation

Open up the folder location of your Anaconda installation. 
Open the settings of the Anaconda Prompt.
Change the path, that it's pointing to.

From: 
%windir%\System32\cmd.exe "/K" C:\Users\username\Anaconda3\Scripts\activate.bat C:\Users\username\Anaconda3\envs\your_env

To:
C:\Users\username\Anaconda3\pythonw.exe C:\path_to_file\cwp_environ_set_proxy_gui.py C:\Users\username\Anaconda3 %windir%\System32\cmd.exe "/K" C:\Users\username\Anaconda3\Scripts\activate.bat C:\Users\username\Anaconda3\envs\your_env

