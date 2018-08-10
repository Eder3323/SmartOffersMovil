package com.example.ed.smartoffers;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.content.pm.Signature;
import android.support.v4.view.ViewCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.facebook.AccessToken;
import com.facebook.CallbackManager;
import com.facebook.FacebookCallback;
import com.facebook.FacebookException;
import com.facebook.GraphRequest;
import com.facebook.GraphResponse;
import com.facebook.login.LoginResult;
import com.facebook.login.widget.LoginButton;
import com.squareup.picasso.Picasso;
import org.json.JSONException;
import org.json.JSONObject;
import java.net.MalformedURLException;
import java.net.URL;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.Principal;
import java.util.Arrays;
import java.util.logging.Handler;

public class LoginActivity extends AppCompatActivity {

    Button botonConfirmar;
    ////Facebook Login //////////////
    CallbackManager callbackManager;
    TextView txtIdFace;
    EditText user_Email, userPass;
    ProgressDialog mDialog;
     String someVariable;

  //  private Session sessionhola;//global variable
    //sessionhola = new Session(); //in oncreate
//and now we set sharedpreference then use this like



    public Intent Log_Principal,Log_Admin;

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode,resultCode,data);
        callbackManager.onActivityResult(requestCode,resultCode,data);

    }
    ///////////////////////////// END FACEBOOK LOGIN

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        user_Email= (EditText)findViewById(R.id.txtCorreo);
        userPass=(EditText)findViewById(R.id.txtContraseña);

        Log_Principal = new Intent(this, Principal_QR.class);
        Log_Admin = new Intent(this, AdminActivity.class);
        botonConfirmar=(Button)findViewById(R.id.btnConfirmar);

        //Facebook Login
        callbackManager=CallbackManager.Factory.create();
        txtIdFace=(TextView)findViewById(R.id.txtId);



        final LoginButton loginButton=(LoginButton)findViewById(R.id.login_button);
        loginButton.setReadPermissions(Arrays.asList("public_profile","email","user_birthday"));


        loginButton.registerCallback(callbackManager, new FacebookCallback<LoginResult>() {
            //if already login


            @Override
            public void onSuccess(LoginResult loginResult) {
                mDialog=new ProgressDialog(LoginActivity.this);
                mDialog.setMessage("Retrieving data...");
                mDialog.show();

                GraphRequest request=GraphRequest.newMeRequest(loginResult.getAccessToken(), new GraphRequest.GraphJSONObjectCallback() {
                    @Override
                    public void onCompleted(JSONObject object, GraphResponse response) {
                        mDialog.dismiss();
                        Log.d("response",response.toString());
                        getData(object);
                    }
                });
                //request  Graph API
                Bundle parameters=new Bundle();
                parameters.putString("fields","id,email,birthday");
                request.setParameters(parameters);
                request.executeAsync();
            }

            @Override
            public void onCancel() {
                Toast.makeText(LoginActivity.this,"El logueo ha sido cancelado", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onError(FacebookException error) {
                Toast.makeText(LoginActivity.this,"Encontramos un Error!!::. Intente más tarde", Toast.LENGTH_SHORT).show();
            }
        });
        if(AccessToken. getCurrentAccessToken() != null)
        {
            txtIdFace.setText(AccessToken.getCurrentAccessToken().getUserId());
            //startActivity(Log_Principal);
            String Idtoken=AccessToken.getCurrentAccessToken().getUserId();

            Intent intent=new Intent(LoginActivity.this, AdminActivity.class);
            intent.putExtra("idtoken", Idtoken);
            startActivity(intent);
        }
        /////End Facebook Login
        botonConfirmar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try{
                    if (user_Email.getText().equals("") || userPass.getText().equals("")) {
                        Toast.makeText(LoginActivity.this,"Por favor introduzca usuario y/o contraseña!!", Toast.LENGTH_SHORT).show();

                    }else {
                       // String user = user_Email.getText().toString();
                        //String pass = userPass.getText().toString();
                        String user = "admin";
                        String pass = "password";

                        if(user.equals("user") && pass.equals("password")){

                            startActivity(Log_Principal);
                        }else if(user.equals("admin") && pass.equals("password")){
                            startActivity(Log_Admin);
                        }
                        else{
                            Toast.makeText(LoginActivity.this,"Usuario o Clave incorrecta..!!", Toast.LENGTH_SHORT).show();

                        }
                    }
                }catch(Exception e){
                    Toast.makeText(LoginActivity.this,"Error...\n"+e, Toast.LENGTH_SHORT).show();
                }
            }
        });

    }

    /////Facebook Login
    private void getData(JSONObject object) {
        try {
            URL profile_picture=new URL("https://graph.facebook.com/"+object.getString("id")+"/picture?width=250&height=250");
            //my metod
            String txtmail=object.getString("email");
            String txtcumple=object.getString("birthday");

            if (txtmail.equals("")&txtcumple.equals("")){

                Toast.makeText(LoginActivity.this,"Error al obtener Datos de Facebook!!", Toast.LENGTH_SHORT).show();
            }else {
                Intent intent=new Intent(LoginActivity.this, Principal_QR.class);
                intent.putExtra("hello",profile_picture.toString());
                intent.putExtra("mail", txtmail);
                intent.putExtra("cumple", txtcumple);
                intent.putExtra("id",AccessToken.getCurrentAccessToken().getUserId());
                startActivity(intent);

              //someVari|ble=AccessToken.getCurrentAccessToken().getUserId();
               // session.setusename(someVariable);
            }

        } catch (MalformedURLException e) {

        } catch (JSONException e) {

        }
    }


    private void printKeyHash() {

        try{
            PackageInfo info= getPackageManager().getPackageInfo("com.example.ed.smartoffers", PackageManager.GET_SIGNATURES);
            for (Signature signature:info.signatures)
            {
                MessageDigest md=MessageDigest.getInstance("SHA");
                md.update(signature.toByteArray());
                Log.d( "KeyHash", Base64.encodeToString(md.digest(),Base64.DEFAULT));

            }
        } catch (PackageManager.NameNotFoundException e) {

        } catch (NoSuchAlgorithmException e) {

        }
    }
    /////End Facebook Login
}
