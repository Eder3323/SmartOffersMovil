package com.example.ed.smartoffers;

import android.content.Intent;
import android.graphics.Bitmap;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;
import com.journeyapps.barcodescanner.BarcodeEncoder;
import com.squareup.picasso.Picasso;

public class Principal_QR extends AppCompatActivity {

    TextView txtmail, txtcumple,id;
    ImageView imgAvatar,image;

    Button gen_btn;
String text2Qr;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_principal__qr);

        image= (ImageView) findViewById(R.id.image);
        txtmail=(TextView) findViewById(R.id.txtEmail);
        gen_btn= (Button)findViewById(R.id.btnConfirmar);
        imgAvatar=(ImageView)findViewById(R.id.avatar);
        txtcumple=(TextView) findViewById(R.id.txtBirtday);
        id=(TextView) findViewById(R.id.txtId);

        Bundle men=getIntent().getExtras();
        txtmail.setText(men.getString("mail"));
        txtcumple.setText(men.getString("cumple"));
        Picasso.with(this).load(men.getString("hello")).into(imgAvatar);

        //id.setText(men.getString("id"));

///QR CODE
        text2Qr="SmartOffersQR_"+txtmail.getText().toString().trim()+"_"+txtcumple.getText().toString().trim();

        MultiFormatWriter multiFormatWriter=new MultiFormatWriter();
        try {
            BitMatrix bitMatrix=multiFormatWriter.encode(text2Qr, BarcodeFormat.QR_CODE,200,200);
            BarcodeEncoder barcodeEncoder=new BarcodeEncoder();
            Bitmap bitmap=barcodeEncoder.createBitmap(bitMatrix);
            image.setImageBitmap(bitmap);

        } catch (WriterException e) {
            e.printStackTrace();
        }
        //END QR CODE

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


