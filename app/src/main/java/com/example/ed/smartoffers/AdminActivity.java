package com.example.ed.smartoffers;

import android.Manifest;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.ImageFormat;
import android.net.Uri;
import android.os.Build;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.zxing.Result;
import com.squareup.picasso.Picasso;

import me.dm7.barcodescanner.zxing.ZXingScannerView;

import static android.Manifest.permission.CAMERA;

public class AdminActivity extends AppCompatActivity implements ZXingScannerView.ResultHandler {
   // TextView id;

    //Button qr;
    private Session sessionhola;//global variable

private static final int REQUET_CAMERA=1;
    private ZXingScannerView scannerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_admin);

        scannerView=new ZXingScannerView(this);
        setContentView(scannerView);

        //if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (checkPermission()){

                Toast.makeText(AdminActivity.this,"Permiso Concedido!!", Toast.LENGTH_SHORT).show();
            } else{
                requestPermission();
            }
        //}
/*
        id = (TextView) findViewById(R.id.txtId);
        Bundle men = getIntent().getExtras();
        id.setText(men.getString("idtoken"));
        */
    }


    private boolean checkPermission() {
        return  (ContextCompat.checkSelfPermission(AdminActivity.this, Manifest.permission.CAMERA)== PackageManager.PERMISSION_GRANTED);
    }
    private void requestPermission() {
        ActivityCompat.requestPermissions(this, new String[]{CAMERA},REQUET_CAMERA);
    }
    public void onRequestPermissionsResult(int requestCode, String permission[], int grantResults[])
    {
     switch (requestCode)
     {
         case REQUET_CAMERA:
             if (grantResults.length > 0)
             {
                boolean cameraAcepted=grantResults[0]==PackageManager.PERMISSION_GRANTED;
                 if (cameraAcepted)
                 {
                     Toast.makeText(AdminActivity.this,"Permiso Activado!!", Toast.LENGTH_SHORT).show();
                 }
                 else{
                     Toast.makeText(AdminActivity.this,"Permiso Denegado!!", Toast.LENGTH_SHORT).show();
                     if (Build.VERSION.SDK_INT>= Build.VERSION_CODES.M)
                     {
                            if (shouldShowRequestPermissionRationale(CAMERA))
                            {
                                displayAlertMessage("Necesitas dar acceso a Ambos Permisos!..", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                                            requestPermissions(new String[]{CAMERA},  REQUET_CAMERA);
                                        }
                                    }
                                });
                                return;
                            }

                     }
                 }
             }
             break;
     }
    }
    @Override
    public void onResume()
    {
        super.onResume();
        //if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            if (checkPermission())
            {
                if (scannerView==null)
                    {
                        scannerView=new ZXingScannerView(this);
                        setContentView(scannerView);
                    }
                    scannerView.setResultHandler(this);
                scannerView.startCamera();
            }
            else
            {
                requestPermission();
            }

       // }
    }
    @Override
    public void onDestroy(){
        super.onDestroy();
        scannerView.stopCamera();
    }

    public void displayAlertMessage(String message, DialogInterface.OnClickListener listener)
    {
        new AlertDialog.Builder(AdminActivity.this)
                .setMessage(message)
                .setPositiveButton("OK", listener)
                .setNegativeButton("Canacelar", null)
                .create()
                .show();
    }
  @Override
    public void handleResult(Result result) {
            final String scanResult=result.getText();
      AlertDialog.Builder builder=new AlertDialog.Builder(this);
      builder.setTitle("Resultado del Scanner");
      builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
          @Override
          public void onClick(DialogInterface dialog, int which) {
              scannerView.resumeCameraPreview(AdminActivity.this);
          }
      });
      builder.setNeutralButton("Visit", new DialogInterface.OnClickListener() {
          @Override
          public void onClick(DialogInterface dialog, int which) {
              Intent intent =new Intent(Intent.ACTION_VIEW, Uri.parse(scanResult));
              startActivity(intent);

          }
      });
      builder.setMessage(scanResult);
      AlertDialog alert=builder.create();
      alert.show();
    }


}
