package com.example.ed.smartoffers;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class Principal_QR extends AppCompatActivity {
    Button btnSalir, btnAtras;
    TextView txtmail,txtcumple;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_principal__qr);

        btnAtras=(Button)findViewById(R.id.btnAtras);
        btnSalir=(Button)findViewById(R.id.btnSalir);


        txtmail=(TextView) findViewById(R.id.txtEmail);
        txtcumple=(TextView) findViewById(R.id.txtBirtday);

        Bundle men=getIntent().getExtras();
            txtmail.setText(men.getString("mail").toString()+" vs "+men.getString("cumple").toString());




        btnSalir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
        btnAtras.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent=new Intent(Principal_QR.this, LoginActivity.class);
                startActivity(intent);
            }
        });
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


