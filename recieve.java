/*import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class recieve {
    public static void main(String[] args) throws
            IOException {
        //服务器接收数据
        ServerSocket ss=new ServerSocket(10001);
        Socket s=ss.accept();
        //读取视频文件  读取 当前类文件路径下的视频文件
        BufferedInputStream bis=new BufferedInputStream
                (recieve.class.getClassLoader().getResourceAsStream("D:\\desk\\JuniorFirst\\ComputerNetwork\\project\\test.png"));
        BufferedOutputStream bos=new BufferedOutputStream(s.getOutputStream());
        byte[] bytes=new byte[8192];
        int len;
        while ((len=bis.read(bytes))!=-1){
            bos.write(bytes,0,len);
            bos.flush();
        }
        s.shutdownOutput();
        BufferedReader br=new BufferedReader(new InputStreamReader(s.getInputStream()));
        //输出 数据
        System.out.println("客户端："+br.readLine());
        bis.close();
        s.close();
    }
}*/

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class recieve {
    public static void main(String[] args){
        DataInputStream dis=null;
        Socket socket =null;
        FileOutputStream fos =null;
        InputStreamReader ir = null;
        BufferedReader br = null;
        try{
            int length=0;
            byte[] getByte = new byte[1024];
            ServerSocket ss = new ServerSocket(7777);
            System.out.println("服务器创建完毕");
            socket = ss.accept();
            ir=new InputStreamReader(socket.getInputStream());
            br=new BufferedReader(ir);
            System.out.println("连接到客户端");
            dis = new DataInputStream(socket.getInputStream());
            File file = new File("D:\\desk\\JuniorFirst\\ComputerNetwork\\project\\test.png");
            fos = new FileOutputStream(file);
            String first = br.readLine();
            String second = br.readLine();
            System.out.println(first);
            System.out.println(second);
            System.out.println("准备接收文件");
            while((length=dis.read(getByte))>0){
                fos.write(getByte, 0, length);
                fos.flush();
            }
            System.out.println("文件接收完毕");
        }catch(IOException e){
            e.getStackTrace();
        }finally{
            try {
                dis.close();
                fos.close();
                socket.close();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
    }
}
