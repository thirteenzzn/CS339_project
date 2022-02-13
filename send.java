/*import java.io.*;
import java.net.InetAddress;
 import java.net.Socket;
 import java.net.UnknownHostException;

public class send {
    public static void main(String[] args) throws
            IOException {
        //这里是客户端
        Socket s = new Socket("192.168.1.103", 10001);
        //使用字节缓冲流接收数据
        //服务器输出数据 ，客户端接收数据保存到数据库中
        BufferedInputStream bis=new BufferedInputStream(s.getInputStream());

        BufferedOutputStream bos=new BufferedOutputStream(new FileOutputStream("D:\\desk\\JuniorFirst\\ComputerNetwork\\project\\1.png"));

        byte[] bytes=new byte[8192];
        int len;
        while ((len=bis.read(bytes))!=-1){
            bos.write(bytes,0,len);
            bos.flush();
        }
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
        //输出 反馈给服务器
        bw.write("我已接收到文件");
        bw.flush();
        bos.close();
        s.close();
    }
}*/

import java.io.*;
import java.net.Socket;
import java.net.UnknownHostException;

public class send {
    public static void main(String[] args){
        int length =0;
        FileInputStream fis = null;
        DataOutputStream dos = null;
        Socket socket = null;
        OutputStream out =null;
        PrintWriter pw = null;
        byte[] sendByte = null;
        try {
            socket = new Socket("localhost",7777);
            out = socket.getOutputStream();
            pw = new PrintWriter(out);
            System.out.println("连接到服务器成功");
            File file = new File("D:\\desk\\JuniorFirst\\ComputerNetwork\\project\\1.png");
            fis = new FileInputStream(file);
            dos = new DataOutputStream(socket.getOutputStream());
            sendByte = new byte[1024];
            pw.write("123"+"\r\n");
            pw.flush();
            pw.write("456"+"\r\n");
            pw.flush();
            System.out.println("准备发送");
            while((length=fis.read(sendByte))>0){
                dos.write(sendByte, 0 , length);
                dos.flush();
            }
            System.out.println("文件发送完毕");
        } catch (UnknownHostException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }finally{
            try {
                fis.close();
                dos.close();
                socket.close();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
    }
}
