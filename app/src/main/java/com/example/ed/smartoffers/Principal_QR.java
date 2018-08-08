package com.example.ed.smartoffers;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

public class Principal_QR extends AppCompatActivity {

    TextView txtmail,txtcumple;
    ImageView imgAvatar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_principal__qr);

        imgAvatar=(ImageView)findViewById(R.id.avatar);

        txtmail=(TextView) findViewById(R.id.txtEmail);
        txtcumple=(TextView) findViewById(R.id.txtBirtday);

        Bundle men=getIntent().getExtras();
            txtmail.setText(men.getString("mail"));
            txtcumple.setText(men.getString("cumple"));
             Picasso.with(this).load(men.getString("hello")).into(imgAvatar);

    }
    //Cuando presionas la tecla de ATRAS no pasara nada con esté método onBackPressed
    @Override
    public void onBackPressed() {
        /* if (!shouldAllowBack()) {
            doSomething();
        } else {
            super.onBackPressed();
        }
        */
    }

}


