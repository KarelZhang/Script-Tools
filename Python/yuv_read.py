from numpy import *

screenLevels = 255.0
def yuv_import(filename,dims,numfrm,startfrm):
    fp=open(filename,'rb')
    blk_size = int(prod(dims) *3/2)
    fp.seek(blk_size*startfrm, 0)
    Y=[]
    U=[]
    V=[]

    d00=dims[0]//2
    d01=dims[1]//2

    Yt=zeros((dims[0],dims[1]),uint8,'C')
    Ut=zeros((d00,d01),uint8,'C')
    Vt=zeros((d00,d01),uint8,'C')
    for i in range(numfrm):
        for m in range(dims[0]):
            for n in range(dims[1]):
                #print m,n
                Yt[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Ut[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Vt[m,n]=ord(fp.read(1))
        Y=Y+[Yt]
        U=U+[Ut]
        V=V+[Vt]
    fp.close()
    return (Y,U,V)
if __name__ == '__main__':
    width=1920
    height=1080
    data_damage =yuv_import('D:\zja\data/mg_train_0000_damage.yuv',(height,width),1,100)

    data_ref = yuv_import('D:\zja\data/mg_train_0000_ref.yuv', (height, width), 1, 100)
    # cv2.imshow("sohow",YY)
    # cv2.waitKey(0)
    u_1 = data_damage[2][0]
    u_2 = data_ref[2][0]

    print((u_1 - u_2).shape)
