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

public class LoginActivity extends AppCompatActivity {

    Button botonConfirmar;
    ////Facebook Login //////////////
    CallbackManager callbackManager;
    TextView txtEmail,txtBirth,txtFriends,txtIdFace;
    ProgressDialog mDialog;
    ImageView imgAvatar;

    public Intent Log_Principal;

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

        Log_Principal = new Intent(this, Principal_QR.class);
        botonConfirmar=(Button)findViewById(R.id.btnConfirmar);
        //Facebook Login
        callbackManager=CallbackManager.Factory.create();
        txtBirth=(TextView)findViewById(R.id.txtBirtday);
        txtEmail=(TextView)findViewById(R.id.txtEmail);
        txtFriends=(TextView)findViewById(R.id.txtFriends);
        txtIdFace=(TextView)findViewById(R.id.txtId);

        imgAvatar=(ImageView)findViewById(R.id.avatar);


        final LoginButton loginButton=(LoginButton)findViewById(R.id.login_button);
        loginButton.setReadPermissions(Arrays.asList("public_profile","email","user_birthday","user_friends"));


        loginButton.registerCallback(callbackManager, new FacebookCallback<LoginResult>() {
            //if already login


            @Override
            public void onSuccess(LoginResult loginResult) {
                mDialog=new ProgressDialog(LoginActivity.this);
                mDialog.setMessage("Retrieving data...");
                mDialog.show();

                String accesstoken=loginResult.getAccessToken().getToken();
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
                parameters.putString("fields","id,email,birthday,friends");
                request.setParameters(parameters);
                request.executeAsync();
            }

            @Override
            public void onCancel() {

            }

            @Override
            public void onError(FacebookException error) {

            }
        });
        if(AccessToken. getCurrentAccessToken() != null)
        {
            txtIdFace.setText(AccessToken.getCurrentAccessToken().getUserId());
            //startActivity(Log_Principal);
        }
        /////End Facebook Login
        botonConfirmar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String txtmail=txtEmail.getText().toString();
                String txtcumple=txtBirth.getText().toString();

                if (txtmail.equals("")&txtcumple.equals("")){

                    Toast.makeText(LoginActivity.this,"Primero tiene quen Loguearse por medio del boton de Facebook...", Toast.LENGTH_SHORT).show();
                }else {
                    Intent intent=new Intent(LoginActivity.this, Principal_QR.class);
                    intent.putExtra("mail", txtmail);
                    intent.putExtra("cumple", txtcumple);
                    startActivity(intent);
                }

            }
        });
    }
    /////Facebook Login
    private void getData(JSONObject object) {
        try {
            URL profile_picture=new URL("https://graph.facebook.com/"+object.getString("id")+"/picture?width=250&height=250");

            Picasso.with(this).load(profile_picture.toString()).into(imgAvatar);

            txtEmail.setText(object.getString("email"));
            txtBirth.setText(object.getString("birthday"));
            txtFriends.setText("Friends: "+object.getJSONObject("friends").getJSONObject("summary").getString("total_count") );

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
