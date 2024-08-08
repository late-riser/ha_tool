import os
import shutil


class dircreator:
    def __init__(self, chara, version, alt):
        self.chara = chara
        self.version =  version
        self.alt = alt
    
    def __str__(self):
        newdir = f"ha_{self.chara}_{self.version}{self.alt}"
        return newdir
    
    def charaSearch(self):
        for i in os.listdir(direc):
            if self.chara in i:
                print(i)
        
    
class folderDir:
    def __init__(self, sname, fname, bigfname, haname):
        self.sname = sname
        self.fname = fname
        self.bigfname = bigfname
        self.haname = haname
        
    def foldermaker(self):
        dd = os.path.expanduser("~/Documents")
        os.chdir(dd)
        filer = f"{dd}/{self.sname}/tex/system/{self.haname}/{self.fname}_ifs"
        shutil.copytree(self.bigfname , filer)
        os.chdir(filer)
        
    def origirem(self):
        dd = os.path.expanduser("~/Documents")
        filer = f"{dd}/{self.sname}/tex/system/{self.haname}/{self.fname}_ifs/tex/{self.fname}.png"
        if os.path.exists(filer) == True:
            os.remove(filer)
        else:
            pass 
               
class postFold:
        def __init__(self, photodir, photoname, sname, fname,haname):
            self.sname = sname
            self.photodir = photodir
            self.photoname = photoname
            self.fname = fname
            self.haname = haname
            
        def photorep(self):
            dd = os.path.expanduser("~/Documents")
            shutil.copy(self.photodir, f"{dd}/{self.sname}/tex/system/{self.haname}/{self.fname}_ifs/tex")
            os.rename(f"{dd}/{self.sname}/tex/system/{self.haname}/{self.fname}_ifs/tex/{self.photoname}", f"{dd}/{self.sname}/tex/system/{self.haname}/{self.fname}_ifs/tex/{self.fname}.png")
            

        
working =  True

while working:
        direc = input("Which ha directory would you like to use\nType END to end\n")
        if direc == "END":
            break
        else:
            if os.path.exists(direc) == True:
                os.chdir(direc)
                haname = os.path.basename(direc)
                chara = input("Which character would you like to change\n")
                chara = chara.lower()
                version = input("Which version\n")
                if version.isdigit() == True:
                    altc = input("Which alt would you like to replace (a , b, etc., leave blank if no alt)\n")
                    ##old mod name place
                    newdir = dircreator(chara,version,altc)
                    newdirbig = F"{direc}\\{newdir}_ifs"
                    if os.path.exists(newdirbig) ==True:
                        modname = input("Name your mod\n")
                        modname = modname.lower()
                        os.chdir(newdirbig)
                        eek = folderDir(modname,newdir,newdirbig,haname)
                        
                        folderDir.foldermaker(eek)
                        folderDir.origirem(eek)
                        
                        picdir = input("Which image would you like to use?\nPlease use a PNG that is '250x322' or '382x502'\n")
                        if os.path.exists(picdir) == True:
                            photoname = os.path.basename(picdir)
                                
                            wawa = postFold(picdir,photoname, modname, newdir,haname)
                            postFold.photorep(wawa)
                            
                            dd = os.path.expanduser("~/Documents")
                            print(f"Your file is stored at '{dd}/{modname}'\nPlease copy into data_mods or repack into IFS\n")
                        else:
                            print("This file does not exist\n")
                    else:
                        print("There was an error in chara, ver, alt input")
                        print("possible charcter files")
                        dircreator.charaSearch(newdir)
                else:
                    print("Please use a number here\n")
            else:
                print("Invalid directory\n")

            



                