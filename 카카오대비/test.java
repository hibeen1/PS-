import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

import javax.net.ssl.HttpsURLConnection;

/**
 * test
 */
public class test {

    public static void main(String[] args) {
        try {
            String req = "https://jsonmock.hackerrank.com/api/countries?name=" + country;
            URL url = new URL(req);    
            HttpsURLConnection conn = (HttpsURLConnection)url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-Type", "application/json");
            System.out.println(conn.getResponseCode());
            
            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            JSONOb
            
            
        } catch (Exception e) {
            System.out.println("error");
        }
        
    }
    
}